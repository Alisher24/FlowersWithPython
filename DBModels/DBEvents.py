from sqlalchemy import event
from DBModels.Bouquet import Bouquet
from DBModels.Florist import Florist
from DBModels.Base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Создаем двигатель и сессию для использования в обработчике событий
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)

# Глобальная переменная для хранения состояния о том, что был вставлен букет
bouquet_inserted = False

@event.listens_for(Bouquet, 'after_insert')
def after_insert_listener(mapper, connection, target):
    global bouquet_inserted
    bouquet_inserted = True

@event.listens_for(sessionmaker, 'after_flush')
def after_flush_listener(session, flush_context):
    global bouquet_inserted
    if bouquet_inserted:
        try:
            florist_id = session.new[0].florist_id  # Получаем florist_id из нового объекта
            if florist_id:
                florist = session.query(Florist).filter_by(id=florist_id).first()
                if florist:
                    florist.numberOfCollectedBouquets += 1
                    session.commit()
                    print(f"Updated bouquets collected for florist {florist_id}.")
                else:
                    print(f"Florist with ID {florist_id} not found.")
            else:
                print("Florist ID not specified for the bouquet.")
        except Exception as e:
            print(f"Error updating florist: {e}")
            session.rollback()
        finally:
            bouquet_inserted = False  # Сбрасываем флаг после обработки
