from django.shortcuts import get_object_or_404, redirect, render

from .models import Memo


# 메모 페이지
def memo(request):
    memos = Memo.objects.all().order_by("-created_at")
    return render(request, "memo/memo.html", {"memos": memos})


# 메모 추가
def memo_create(request):
    if request.method == "POST":
        content = request.POST.get("content")
        Memo.objects.create(content=content)  # DB에 저장
    return redirect("memo")  # 메모 페이지로 이동


# 메모 삭제
def memo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    memo.delete()
    return redirect("memo")
