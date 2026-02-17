#This file handles HTTP requests related to members.
# 
# #POST	/members
#GET	/members
#GET	/members/{id}
#PUT	/members/{id}
#DELETE	/members/{id}



from app.domain.services.member_service import MemberService
from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from library_management.app.validators.member_model import (MemberCreate,
                                                            MemberUpdate)

#Creates route group named member_bp to be registerd inside main.py.
member_bp = Blueprint("member_bp", __name__)

# Create Member
@member_bp.route("/", methods=["POST"])
def add_member():
    try:

        data = MemberCreate(**request.json)

        member = MemberService.add_member(
            name=data.name,
            email=data.email
        )
        return jsonify(member), 201 #Convert result to JSON, HTTP 201 means Created successfully

    except ValidationError as err:
        return {"error": err.messages}, 400




#Get All Members
@member_bp.route("/", methods=["GET"])
def get_members():

    limit = int(request.args.get("limit", 10))
    offset = int(request.args.get("offset", 0))
    search = request.args.get("search")

    members = MemberService.get_all_members(limit, offset, search)

    return jsonify(members), 200


# Get Member by ID
@member_bp.route("/<member_id>", methods=["GET"])
def get_member(member_id):
    member = MemberService.get_member(member_id)
    return jsonify(member), 200

# Update Member
@member_bp.route("/<member_id>", methods=["PUT"])
def update_member(member_id):
    try:

        data = MemberUpdate(**request.json)

        updated_member = MemberService.update_member(
            member_id,
            **data.dict(exclude_unset=True)
        )

        return jsonify(updated_member), 200

    except ValidationError as err:
        return {"error": err.messages}, 400


# Delete Member
@member_bp.route("/<member_id>", methods=["DELETE"])
def delete_member(member_id):
    MemberService.delete_member(member_id)
    return jsonify({"message": "Member deleted successfully"}), 200
