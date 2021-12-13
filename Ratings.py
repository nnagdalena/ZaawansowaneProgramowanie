from typing import List
from flask_restful import Resource
import csv


class Rating:

    def __init__(self, user_id: str, movie_id: str, rating: str, timestamp: str):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"userid: {self.userId}, movieid: {self.movieId}, " \
               f"rating: {self.rating}, timestamp: {self.timestamp}"


class Ratings(Resource):

    ratings: List[Rating] = []

    def __init__(self) -> None:
        super().__init__()
        with open("ratings.csv", newline='') as csv_file:
            rating_rows = csv.reader(csv_file, delimiter=",")
            for row in rating_rows:
                self.ratings.append(Rating(row[0], row[1], row[2], row[3]))

    def get(self):
        return [rating.__dict__ for rating in self.ratings[1:]]
