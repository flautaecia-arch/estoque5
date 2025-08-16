from flask import Blueprint, jsonify
from src.models.produto import Produto
from src.models.lote import Lote
from src.models.user import db
import os

debug_bp = Blueprint('debug', __name__, url_prefix='/api/debug')

@debug_bp.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar a saúde do banco de dados"""
    try:
        # Verificar se o banco de dados está acessível
        db.session.execute('SELECT 1')
        
        # Contar produtos
        total_produtos = Produto.query.count()
        
        # Contar lotes
        total_lotes = Lote.query.count()
        
        # Verificar se o arquivo do banco existe
        db_path = db.engine.url.database
        db_exists = os.path.exists(db_path) if db_path else False
        
        # Listar alguns produtos para debug
        produtos_sample = []
        produtos = Produto.query.limit(10).all()
        for produto in produtos:
            produtos_sample.append({
                'codigo': produto.codigo,
                'nome': produto.nome
            })
        
        return jsonify({
            'status': 'healthy',
            'database': {
                'accessible': True,
                'path': db_path,
                'file_exists': db_exists,
                'total_produtos': total_produtos,
                'total_lotes': total_lotes
            },
            'produtos_sample': produtos_sample,
            'environment': {
                'DATABASE_DIR': os.environ.get('DATABASE_DIR', 'not_set'),
                'PORT': os.environ.get('PORT', 'not_set')
            }
        })
        
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'database': {
                'accessible': False,
                'path': getattr(db.engine.url, 'database', 'unknown'),
                'file_exists': False
            },
            'environment': {
                'DATABASE_DIR': os.environ.get('DATABASE_DIR', 'not_set'),
                'PORT': os.environ.get('PORT', 'not_set')
            }
        }), 500

@debug_bp.route('/produtos', methods=['GET'])
def list_all_produtos():
    """Endpoint para listar todos os produtos no banco"""
    try:
        produtos = Produto.query.all()
        produtos_list = []
        
        for produto in produtos:
            produtos_list.append({
                'codigo': produto.codigo,
                'nome': produto.nome
            })
        
        return jsonify({
            'total': len(produtos_list),
            'produtos': produtos_list
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@debug_bp.route('/produto/<codigo>', methods=['GET'])
def get_produto_by_codigo(codigo):
    """Endpoint para buscar um produto específico por código"""
    try:
        produto = Produto.query.filter_by(codigo=codigo).first()
        
        if produto:
            return jsonify({
                'found': True,
                'produto': {
                    'codigo': produto.codigo,
                    'nome': produto.nome
                }
            })
        else:
            return jsonify({
                'found': False,
                'codigo_buscado': codigo
            })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@debug_bp.route('/reinit', methods=['POST'])
def reinitialize_database():
    """Endpoint para reinicializar o banco de dados (apenas para debug)"""
    try:
        # Limpar produtos existentes
        db.session.query(Produto).delete()
        db.session.commit()
        
        # Dados dos produtos (alguns para teste)
        produtos_data = [
            ("12", "LOCAO HIDR.PE MAGIC GLAMOUR 200 ML"),
            ("1558", "EDT PE NUMBER ONE 100 ML"),
            ("2555", "EDT PE BLACK SHARK 100 ML"),
            ("2678", "EDT PE BILLION $ 100 ML"),
            ("3170", "EDT PE BLUE CAVIAR 100 ML")
        ]
        
        # Inserir produtos
        for codigo, nome in produtos_data:
            produto = Produto(codigo=codigo, nome=nome)
            db.session.add(produto)
        
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': f'Banco reinicializado com {len(produtos_data)} produtos'
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

