import random
themes = {
    'Adventure': ['treasure hunt', ],
    'Friendship': ['making new friends', ],
    'Environment': ['saving the forest', ],
    'Culture': ['festivals around the world', ]}

protagonists = ['a young inventor', 'a talking tree', 'a friendly robot']
antagonists = ['a mischievous goblin', 'a greedy giant', 'a cunning fox']
conflicts = ['overcoming a fear', 'solving a mystery', 'stopping a villain']
resolutions = ['learning a lesson', 'achieving a goal', 'making new friends']

educational_topics = ['the water cycle', 'basic arithmetic', 'ancient Egypt', 'the solar system']

moral_lessons = ['honesty', 'kindness', 'responsibility', 'courage', 'respect']


events = {
    'Spring': ['Planting gardens', 'spring cleaning', 'blooming flowers', 'baby animals', 'rain showers', 'picnics', 'kite flying', 'Easter egg hunts', 'nature walks', 'bird watching', 'celebrating Earth Day', 'spring festivals', 'butterfly migrations', 'rainy day activities', 'allergies and remedies'],
    'Summer': ['Beach trips', 'swimming', 'camping', 'fishing', 'summer sports', 'ice cream treats', 'outdoor games', 'gardening', 'hiking', 'summer camps', 'barbecues', 'fireflies at night', 'lemonade stands', 'festivals', 'fireworks', 'stargazing', 'surfing', 'boating', 'water parks', 'summer reading'],
    'Autumn': ['Leaf peeping', 'apple picking', 'harvest festivals', 'Halloween celebrations', 'pumpkin carving', 'corn mazes', 'baking pies', 'back-to-school', 'Thanksgiving', 'collecting acorns', 'hayrides', 'bonfires', 'sweater weather', 'migrating birds', 'preparing for winter', 'scarecrow making'],
    'Winter': ['Snowball fights', 'building snowmen', 'ice skating', 'sledding', 'winter holidays', 'hot cocoa by the fire', 'gift-giving', 'making snow angels', 'winter sports', 'holiday decorations', 'cozy storytelling', 'winter solstice', 'knitting scarves', 'feeding winter birds', "New Year's celebrations"],
    "New Year's Day": ['Making resolutions', 'fireworks', 'celebrating new beginnings', 'cultural traditions', 'countdowns', "New Year's parades", 'family gatherings', 'cleaning and preparing for the new year', 'global celebrations']
}


class Prompt:
    def __init__(self):
        self.prompt = "Hi"

    def generate_event_prompt(self):
        season_or_holiday = random.choice(list(events.keys()))
        activity = random.choice(events[season_or_holiday]) if isinstance(events[season_or_holiday], list) else events[
            season_or_holiday]
        prompt = (
            f"Write a children's story set during {season_or_holiday.lower()}. "
            f"The story involves {activity} and is suitable for children aged 5-7."
        )
        return prompt

