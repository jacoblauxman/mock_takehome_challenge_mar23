from app.models import db, Post, environment, SCHEMA
import random

def seed_posts():
    titles = ['One Cup is All it Takes', 'The Best Cup Ever', 'Mmmmm Mmmm', 'Never Again', 'Be Still, My Brain and Brew', 'Glorious', 'Just Amazing']
    texts = [
    "What would you say a post is really worth? I'd say it's roughly equivalent to however much I'm being paid to currently write these words. More so than anything, it's content, and what more could you ask for?",
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu",
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu",
    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta.",
    "Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pro",
    "Short and sweet. To break up the monotony. Cheers",
    "Leaving a little note now to remind me to come back and finish this post later. Stay tuned! Find out next time on..."
    ]
    ratings = [1,2,3,4,5,5,4,3]
    coffee_ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    for i in range(125):
        new_post = Post(
            title=random.choice(titles),
            text=random.choice(texts),
            rating=random.choice(ratings),
            coffee_id=random.choice(coffee_ids)
        )

        db.session.add(new_post)
        db.session.commit()



def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM posts")

    db.session.commit()
