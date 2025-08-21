docker  build -t achiya31444/mongo-pandas-test-project:1.0 .
docker push achiya31444/mongo-pandas-test-project:1.0
oc create deployment tweettt --image=docker.io/achiya31444/mongo-pandas-test-project:1.0
