docker pull jherup22/cs333-final-project
docker rm -f flashcard_app
docker run --name flashcard_app -itd jherup22/cs333-final-project
docker stop flashcard_app
