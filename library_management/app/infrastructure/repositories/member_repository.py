#-------------------------#
#Main Functions:
#create_member() //add
#get_member_by_id()
#get_member_by_email()
#get_all_members()
#update_member()
#delete_member()
 
#Note: I have add finaly to make sure that Connections always closed even if there are any exception with database connection/ table .. 
#-------------------------#

#disable SQLAlchemy INFO logs for cleaner output
import logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)



from sqlalchemy import insert, select, update, delete,or_
from app.domain.models.member import members
from app.infrastructure.db import get_connection
from app.helper import help_function
from sqlalchemy.exc import SQLAlchemyError



#Create Member
#Adds a new member
def create_member(data):
    conn = get_connection()
    try:
        stmt = insert(members).values(**data)
        result = conn.execute(stmt)
        conn.commit()
        return result.inserted_primary_key[0] #Returning member_id (UUID)
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()


#Get Member By ID 
#Retrieves member using UUID
def get_member_by_id(member_id):
    conn = get_connection()
    try:
        stmt = select(members).where(members.c.member_id == member_id)
        result = conn.execute(stmt).fetchone()
        return help_function.row_to_dict(result) #Returning Dictionary OR None
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()

 
#Get Member By Email
#this function is used for Email uniqueness validation
def get_member_by_email(email):
    conn = get_connection()
    try:
        stmt = select(members).where(members.c.email == email)
        result = conn.execute(stmt).fetchone()
        return help_function.row_to_dict(result)
        
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()



#Get All Members :Pagination + Search
def get_all_members(limit=10, offset=0, search=None):
    conn = get_connection()
    try:
        query = select(members)

        if search:
            query = query.where(
            or_( #ilike : case insensitive search
            members.c.name.ilike(f"%{search}%"),
            members.c.email.ilike(f"%{search}%")
                    )
                )

        query = query.limit(limit).offset(offset)

        result = conn.execute(query)


        return [help_function.row_to_dict(row) for row in result] #Returning List of members
        
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()





# Update Member
def update_member(member_id, data):
    conn = get_connection()
    try:
        stmt = (
            update(members)
            .where(members.c.member_id == member_id)
            .values(**data)
            .returning(members)
        )
        result = conn.execute(stmt).fetchone()
        conn.commit()
        return help_function.row_to_dict(result) #Returns updated member record
    
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()


#Delete Member
#Returning value is True or False:
#True: if the record exists and the member is deleted
#False: if the member record is not found
def delete_member(member_id):
    conn = get_connection()
    try:
        stmt = delete(members).where(members.c.member_id == member_id)

        result = conn.execute(stmt)
        conn.commit()

        return result.rowcount > 0
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()
