import os
import sys
import pandas as pd

# Adicionar o diretório pai ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import app
from src.models.produto import Produto
from src.models.user import db

def setup_production():
    """Configura o banco de dados para produção"""
    
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()
        
        # Limpar produtos existentes antes de adicionar novos
        db.session.query(Produto).delete()
        db.session.commit()
        print("Produtos existentes limpos do banco de dados.")
        
        # Dados dos produtos (extraídos do Excel original)
        produtos_data = [
            ("12", "LOCAO HIDR.PE MAGIC GLAMOUR 200 ML"),
            ("13", "EDP PE D&S VANILLE/FRAMBOISE 60 ML"),
            ("20", "EDP PE D&S CHOCO/MENTHE 60 ML"),
            ("29", "LOCAO HIDR.PE SENSUAL LOVE 200 ML"),
            ("36", "LOCAO HIDR.PE SWEET ANGEL 200 ML"),
            ("37", "EDP PE D&S PATCHOULI 60 ML"),
            ("44", "EDP PE D&S VANILLE/PATCHOULI 60 ML"),
            ("51", "EDP PE D&S CHOCO/VANILLE 60 ML"),
            ("58", "EDP PE D&S FRAMBOISE/PATCHOULI 60 ML"),
            ("65", "EDP PE D&S MENTHE/FRAMBOISE 60 ML"),
            ("72", "EDP PE D&S CHOCO/PATCHOULI 60 ML"),
            ("79", "EDP PE D&S VANILLE/MENTHE 60 ML"),
            ("86", "LOCAO HIDR.PE SWEET LOVE 200 ML"),
            ("93", "LOCAO HIDR.PE MAGIC LOVE 200 ML"),
            ("100", "LOCAO HIDR.PE SENSUAL ANGEL 200 ML"),
            ("107", "LOCAO HIDR.PE SWEET GLAMOUR 200 ML"),
            ("114", "LOCAO HIDR.PE MAGIC ANGEL 200 ML"),
            ("121", "LOCAO HIDR.PE SENSUAL GLAMOUR 200 ML"),
            ("128", "EDT BY PE CASH $ 100 ML"),
            ("378", "EDT BY PE CASCH WOMAN 100 ML"),
            ("422", "EDT BY PE PEPPER 100 ML"),
            ("453", "EDT BY PE COOL MADAM 100 ML"),
            ("521", "EDT BY PE LILY WHITE 100 ML"),
            ("538", "EDT BY PE WOMAN LOVE 100 ML"),
            ("1206", "EDT PE VODKA DIAM.100 ML"),
            ("1213", "EDT PE VODKA EXTR.100 ML"),
            ("1329", "EDT PE MISS ELYSEES 100 ML"),
            ("1497", "EDT PE VODKA LIMITED 100 ML"),
            ("1558", "EDT PE NUMBER ONE 100 ML"),
            ("1633", "EDT PE HANDSOME 100 ML"),
            ("1787", "EDT PE ITS LIFE 100 ML"),
            ("1978", "EDT PE MAX 100 ML"),
            ("2012", "EDT PE AM.TOUJOURS 100 ML"),
            ("2081", "EDT PE NYSE 100 ML"),
            ("2104", "EDT PE MEZZO 100 ML"),
            ("2159", "EDT PE MONSIEUR ELYSEES 100 ML"),
            ("2210", "EDT PE HANDS.BLACK 100 ML"),
            ("2227", "EDT PE SEXY WOMAN 100 ML"),
            ("2272", "EDT PE PINK 100 ML"),
            ("2296", "EDT PE BL.CAVIAR WOMAN 100 ML"),
            ("2548", "EDT PE BL.IS BLACK 100 ML"),
            ("2555", "EDT PE BLACK SHARK 100 ML"),
            ("2630", "EDT PE Y2K 100 ML"),
            ("2678", "EDT PE BILLION $ 100 ML"),
            ("2685", "EDT PE I LOVE PE 100 ML"),
            ("2722", "EDT PE NUITS MAUVES 100 ML"),
            ("2784", "EDT PE GABY 100 ML"),
            ("2791", "EDT PE BLUE SPIRIT 100 ML"),
            ("2838", "EDT PE BILLION WOMAN 100 ML"),
            ("2845", "EDT PE RED GARDEN 100 ML"),
            ("2869", "EDT PE SWEET & STRONG 100 ML"),
            ("2883", "EDT PE RICH AND PRETTY 100 ML"),
            ("2906", "EDT PE VODKA MISS 100 ML"),
            ("2913", "EDT PE VODKA NIGHT 100 ML"),
            ("2920", "EDT PE VODKA MAN 100 ML"),
            ("2937", "EDT PE VODKA PINK 100 ML"),
            ("2944", "EDT PE VODKA THE TIME 100 ML"),
            ("2951", "EDT PE VODKA LOVE 100 ML"),
            ("2968", "EDT PE VODKA BRASIL AZUL 100 ML"),
            ("2975", "EDT PE VODKA BRASIL AMARELO 100 ML"),
            ("3019", "EDT PE LA PETITE FLEUR BLANCHE 100 ML"),
            ("3033", "EDT PE LA PETITE FLEUR D'OR 100 ML"),
            ("3040", "EDT PE LA PETITE FLEUR DE PARI 100 ML"),
            ("3057", "EDT PE LA PETITE FLEUR D'AMOUR 100 ML"),
            ("3064", "EDT PE BILLION CASINO ROYAL 100 ML"),
            ("3071", "EDT PE BILLION RED BOND 100 ML"),
            ("3088", "EDT PE BILLION WOMAN LOVE 100 ML"),
            ("3095", "EDT PE SEXY WOMAN NIGHT 100 ML"),
            ("3101", "EDT PE BILLION $ GREEN BOND BOND 100 ML"),
            ("3118", "EDT PE BILLION $ BLUE JACK 100 ML"),
            ("3125", "EDT PE LPH MYSTERIEUX 100 ML"),
            ("3132", "EDT PE LPH ELEGANT 100 ML"),
            ("3149", "EDT PE LPH GALANT 100 ML"),
            ("3156", "EDT PE LPH SECRET 100 ML"),
            ("3163", "EDT PE LPH DON JUAN 100 ML"),
            ("3170", "EDT PE BLUE CAVIAR 100 ML"),
            ("3187", "EDT PE STYLE CAVIAR 100 ML"),
            ("3194", "EDT PE AMBER CAVIAR 100 ML"),
            ("3200", "EDT PE SILVER CAVIAR 100 ML"),
            ("3217", "EDT PE BLACK CAVIAR 100 ML"),
            ("3224", "EDT PE MISTER CAVIAR 100 ML"),
            ("3231", "EDT PE LA PETITE FLEUR ROMANTIC 100 ML"),
            ("3248", "EDT PE LA PETITE FLEUR SECRETE 100 ML"),
            ("3255", "EDP PE ROMANTIC NIGHT 100 ML"),
            ("3262", "EDP PE ROMANTIC GLAMOUR 100 ML"),
            ("3279", "EDP PE ROMANTIC PRINCESS 100 M"),
            ("3286", "EDP PE ROMANTIC DREAM 100 ML"),
            ("3293", "EDP PE ROMANTIC LOVE 100 ML"),
            ("3354", "EDT PE NIGHT CAVIAR 100 ML"),
            ("3361", "EDT PE LA PETIT FLEUR DE PROVENCE 100 ML"),
            ("3378", "EDT PE VODKA WILD 100 ML"),
            ("3385", "EDT PE BILLION $ NIGHT 100 ML"),
            ("3392", "EDT PE SEXY WOMAN LOVE 100 ML"),
            ("3408", "EDT PE BILLION WOMAN NIGHT 100 ML"),
            ("3415", "EDT PE BLUE MELODY 100 ML"),
            ("3439", "EDT PE BLOODY MARY 100 ML"),
            ("3453", "EDT PE SWEET MAMBO 100 ML"),
            ("3460", "EDT PE INDALA 100 ML"),
            ("3484", "EDT PE DARK CAVIAR 100 ML"),
            ("3491", "EDT PE BILLION $ EXCLUSIVE EDT 100 ML"),
            ("3514", "EDT PE VODKA MYLOS 100 ML"),
            ("3521", "EDT PE VODKA PRIME 100 ML"),
            ("3538", "EDT PE ROUGE ABSOLU 100 ML"),
            ("3545", "EDT PE INDALO 100 ML"),
            ("3552", "EDT PE WOODY MAMBO 100 ML"),
            ("3569", "EDT PE NAUTILUS 100 ML"),
            ("3576", "EDT PE METAMEN 100 ML"),
            ("3583", "EDT PE ONE NIGHT LAS VEGAS 100 ML"),
            ("3590", "EDT PE BOIS D'ELYSEES 100 ML"),
            ("3606", "EDT PE SCENT OF A WOMAN 100 ML"),
            ("3613", "EDT PE SPIRIT OF A WOMAN 100 ML"),
            ("3620", "EDT PE CHARM OF A WOMAN 100 ML"),
            ("3637", "EDT PE TREND OF A WOMAN 100 ML"),
            ("8025", "AGUA MICELAR PARIS ELYSSEES 530 ML")
        ]
        
        # Inserir produtos
        for codigo, nome in produtos_data:
            produto = Produto(codigo=codigo, nome=nome)
            db.session.add(produto)
        
        # Salvar mudanças
        db.session.commit()
        print(f"Produtos inicializados com sucesso! Total: {len(produtos_data)} produtos.")

if __name__ == '__main__':
    setup_production()

