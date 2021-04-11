from quart import jsonify, request
from api.models import Challenge
from .. import bp
import utils
from typing import Union

request: utils.Request


@bp.route("/weekly", methods=["POST"])
@utils.auth_required
@utils.expects_data(
    id=Union[str, int],
    title=str,
    description=str,
    examples=str,
    rules=str,
    difficulty=str,
)
async def post_challenge(
    id: Union[str, int],
    title: str,
    description: str,
    examples: str,
    rules: str,
    difficulty: str,
):

    created_by = request.user_id
    challenge = await Challenge.create(
        id, title, description, examples, rules, created_by, difficulty
    )

    if challenge is None:
        # Challenge already exists
        return (
            jsonify(
                error="Conflict",
                message=f"Challenge with ID {int(id)} already exists.",
            ),
            409,
        )

    return (
        jsonify(
            id=str(challenge.id),
            title=challenge.title,
            description=str(challenge.description),
            examples=challenge.examples,
            rules=challenge.rules,
            created_by=challenge.created_by,
            difficulty=challenge.difficulty,
        ),
        201,
        {"Location": f"/challenges/weekly/{challenge.id}"},
    )


@bp.route("/weekly/<int:weekly_challenge_id>", methods=["GET"])
async def get_challenge(weekly_challenge_id: int):
    """Gets the Weekly Challenge"""

    challenge = await Challenge.fetch_or_404(weekly_challenge_id)

    return jsonify(
        id=str(challenge.id),
        title=challenge.title,
        description=str(challenge.description),
        examples=challenge.examples,
        rules=challenge.rules,
        created_by=str(challenge.created_by),
        difficulty=challenge.difficulty,
    )


@bp.route("/weekly/<int:weekly_challenge_id>", methods=["PATCH"])
@utils.auth_required
async def update_challenge(weekly_challenge_id: int, **data):
    """Update a weekly challenge from its ID"""

    challenge = await Challenge.fetch_or_404(weekly_challenge_id)
    await challenge.update(**data)

    return jsonify(
        id=str(challenge.id),
        title=challenge.title,
        description=str(challenge.description),
        examples=challenge.examples,
        rules=challenge.rules,
        created_by=challenge.created_by,
        difficulty=challenge.difficulty,
    )


@bp.route("/weekly/<int:weekly_challenge_id>", methods=["DELETE"])
@utils.auth_required
async def delete_challenge(weekly_challenge_id: int):
    """Deletes a challenge from its ID"""

    weekly_challenge = await Challenge.fetch_or_404(weekly_challenge_id)
    await weekly_challenge.delete()
    return jsonify("Challenge Deleted", 204)
