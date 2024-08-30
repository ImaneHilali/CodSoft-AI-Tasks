import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class SimpleRecommender:
    def __init__(self):
        # Sample user-item ratings matrix (rows: users, columns: items)
        self.user_item_matrix = np.array([
            [5, 0, 3, 0, 2],
            [4, 0, 4, 3, 1],
            [0, 2, 0, 4, 5],
            [3, 3, 4, 0, 0],
            [5, 0, 0, 3, 4]
        ])
        self.item_descriptions = [
            "Adventure and fantasy",
            "Science fiction and space",
            "Romantic comedy",
            "Thriller and mystery",
            "Documentary and history"
        ]
        self.tfidf_matrix = self._compute_tfidf_matrix()

    def _compute_user_similarity(self):
        user_similarity = cosine_similarity(self.user_item_matrix)
        return user_similarity

    def recommend_by_collaborative_filtering(self, user_index):
        user_similarity = self._compute_user_similarity()
        user_ratings = self.user_item_matrix[user_index]

        scores = user_similarity[user_index] @ self.user_item_matrix

        scores = [(score, index) for index, score in enumerate(scores) if user_ratings[index] == 0]

        scores.sort(reverse=True, key=lambda x: x[0])
        recommendations = [index for _, index in scores]

        return recommendations[:2]  # Return top 2 recommendations

    def _compute_tfidf_matrix(self):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(self.item_descriptions)
        return tfidf_matrix

    def recommend_by_content_based_filtering(self, item_index):
        item_similarity = cosine_similarity(self.tfidf_matrix)
        similar_items = item_similarity[item_index]

        scores = [(score, index) for index, score in enumerate(similar_items) if index != item_index]

        scores.sort(reverse=True, key=lambda x: x[0])
        recommendations = [index for _, index in scores]

        return recommendations[:2]  # Return top 2 recommendations


if __name__ == "__main__":
    recommender = SimpleRecommender()

    # Usage Example:
    print("Collaborative Filtering Recommendations for User 0:")
    collaborative_recommendations = recommender.recommend_by_collaborative_filtering(0)
    print(collaborative_recommendations)

    print("\nContent-Based Filtering Recommendations for Item 1:")
    content_based_recommendations = recommender.recommend_by_content_based_filtering(1)
    print(content_based_recommendations)
