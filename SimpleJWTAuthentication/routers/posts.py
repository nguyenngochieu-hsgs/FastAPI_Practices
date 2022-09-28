from fastapi import APIRouter, HTTPException, Depends
from dependencies import auth

fake_posts = [
    {
        "id": 1,
        "title": "title 1",
        "description": "Description 1"
    },
    {
        "id": 2,
        "title": "title 2",
        "description": "description 2"
    }
]

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    dependencies=[Depends(auth.validate_token)],
    responses = {
        404: {"description": "Not Found"}
    }
)

@router.get("/")
async def get_all_posts(username=Depends(auth.validate_token)):
    return {username: fake_posts}

@router.get("/{post_id}")
async def get_post_by_id(post_id: int, username=Depends(auth.validate_token)):
    for post in fake_posts:
        if post["id"] == post_id:
            return {username: post}
    
    raise HTTPException(status_code=404, detail="Id not found")
