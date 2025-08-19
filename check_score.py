def check_score(score):
    if score >= 90:
        return "🏆 A үнэлгээ"
    elif score >= 75:
        return "🎖 B үнэлгээ"
    elif score >= 60:
        return "📚 C үнэлгээ"
    else:
        return "❌ D үнэлгээ"

scores = [95, 80, 67, 50]
for s in scores:
    print(check_score(s))
