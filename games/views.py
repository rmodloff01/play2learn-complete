import json
from django.http import JsonResponse
from games.models import GameScore

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class GameScoresView(TemplateView):
    template_name = "game-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user_name=self.request.user).order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user_name=self.request.user).order_by('-score')
        return context
    
class LeaderboardView(TemplateView):
    template_name = "leaderboard.html"

    def get_context_data(self, **kwargs):
        context = super(LeaderboardView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context

def record_score(request):
    data = json.load(request.body)

    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]

    new_score = GameScore(user_name=user_name, game=game, score=score)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)