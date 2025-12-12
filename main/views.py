from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings


def home(request):
    """
    Home page view
    """
    return render(request, 'home.html')


def documents(request):
    """
    Documents list view
    """
    return render(request, 'documents.html')


def document_detail(request):
    """
    Document detail view
    """
    return render(request, 'document_detail.html')


def document_edit(request):
    """
    Document edit/create view
    """
    return render(request, 'document_edit.html')


def settings_view(request):
    """
    Settings page view
    """
    return render(request, 'settings.html')

# def syuukatudata_view(request):
#     """
#     SyuuKatuData page view
#     """
#     return render(request, 'syuukatudata.html')

def syuukatudata_view(request):
    """
    バッジコレクション画面
    仮データを使って個数を動的に表示する
    """
    
    # 1. 企業ごとのバッジデータを定義（将来はここをDBから取得するように変える）
    company_data = [
        {
            'name': '株式会社イノベーションテック',
            'color': 'indigo', # UIの装飾用カラー
            'badges': [
                {
                    'title': '長期インターン完遂',
                    'date': '2025/11/01',
                    'short_name': 'IT',
                    'bg_color': '#091398',
                    'is_high_rating': True  # 高評価バッジかどうか
                },
                {
                    'title': '課題解決ワークショップ',
                    'date': '2025/10/05',
                    'short_name': 'W',
                    'bg_color': '#38b48b',
                    'is_high_rating': False
                }
            ]
        },
        {
            'name': '未来クリエイト株式会社',
            'color': 'amber',
            'badges': [
                {
                    'title': '会社説明会参加',
                    'date': '2025/09/15',
                    'short_name': 'FC',
                    'bg_color': '#ffc107',
                    'is_high_rating': False
                }
            ]
        }
    ]

    # 2. データの個数を計算する
    total_badges = 0
    high_rating_count = 0

    for company in company_data:
        # その企業のバッジ数を合計に足す
        total_badges += len(company['badges'])
        # 高評価バッジの数をカウント
        for badge in company['badges']:
            if badge['is_high_rating']:
                high_rating_count += 1

    # 3. テンプレートにデータを渡す
    context = {
        'company_data': company_data,
        'total_badges': total_badges,
        'high_rating_count': high_rating_count,
    }

    return render(request, 'syuukatudata.html', context)


# Legacy view for backward compatibility
def index(request):
    """
    Legacy index page - redirects to home
    """
    return render(request, 'home.html')


def api_hello(request):
    """
    Hello API endpoint
    """
    return JsonResponse({
        'message': 'Hello from Challenge Cara App API!',
        'status': 'success',
        'version': settings.APP_VERSION
    })


def api_status(request):
    """
    Status API endpoint
    """
    return JsonResponse({
        'status': 'running',
        'app': settings.APP_NAME,
        'version': settings.APP_VERSION
    })