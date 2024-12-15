import yaml

# YAML faylını oxumaq
with open('pip.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 1000 səhifədən çox olan kitabları tapmaq
for book in data['books']:
    if book['pages'] > 1000:
        print(f"Big book: {book['title']} from {book['library']}")
