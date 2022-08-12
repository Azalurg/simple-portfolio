from .entities.entity import Session, engine, Base
from .entities.user import User
from datetime import datetime

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = session.query(User).all()

if len(exams) == 0:
    # create and persist mock exam
    today = datetime.now()
    python_exam = User("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script", today)
    session.add(python_exam)
    session.commit()
    session.close()

    # reload exams
    exams = session.query(User).all()

# show existing exams
print('### Exams:')
for exam in exams:
    print(f'({exam.id}) {exam.Username} - {exam.Description}')