from django.shortcuts import get_object_or_404, redirect, render

from .models import Memo


# 메모 페이지
def memo(request):
    # 모든 메모 조회 후 최신 메모가 위에 오도록 정렬
    memos = Memo.objects.all().order_by("-created_at")
    return render(request, "memo/memo.html", {"memos": memos})


# 메모 추가
def memo_create(request):
    if request.method == "POST":
        content = request.POST.get("content")  # 폼에서 content 값 가져오기
        Memo.objects.create(content=content)  # DB에 저장
    return redirect("memo")  # 메모 페이지로 이동


# 메모 삭제
def memo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)  # pk에 해당하는 메모 객체 가져오기, 없으면 404 에러
    memo.delete()  # 메모 삭제
    return redirect("memo")
