# Git Safety Foundation - Vibe Coding

## Giới thiệu

Repository này được tạo ra nhằm mục đích **thực hành và xây dựng nền tảng sử dụng Git & GitHub an toàn**, chuẩn bị cho quá trình Vibe Coding với AI.

---

## 📖 Mục lục

1. [Kiến thức Git cơ bản](#kiến-thức-git-cơ-bản)
2. [GitHub Flow](#github-flow)
3. [Bảo mật GitHub](#bảo-mật-github)
4. [Thực hành Pull Request](#thực-hành-pull-request)
5. [Xử lý Conflict](#xử-lý-conflict)
6. [Revert an toàn](#revert-an-toàn)
7. [Vibe Coding với AI](#vibe-coding-với-ai)

---

## 1. Kiến thức Git cơ bản

Git là **hệ thống quản lý phiên bản phân tán** (Distributed Version Control System).

### Các lệnh cơ bản

| Lệnh | Mô tả |
|------|-------|
| `git init` | Khởi tạo một Git repository cục bộ |
| `git clone <url>` | Sao chép repository từ remote về máy |
| `git status` | Kiểm tra trạng thái các file (untracked, modified, staged) |
| `git add <file>` | Đưa thay đổi vào Staging Area |
| `git commit -m "<message>"` | Ghi lại ảnh chụp trạng thái code với thông điệp |
| `git push origin <branch>` | Đẩy commit lên nhánh tương ứng trên GitHub |
| `git pull origin <branch>` | Kéo và gộp thay đổi mới nhất từ GitHub |
| `git log --oneline` | Xem lịch sử commit rút gọn |

---

## 2. GitHub Flow

Quy trình làm việc chuẩn được áp dụng trong dự án:

- **Branching**: Luôn tạo nhánh mới từ `main` cho mỗi tính năng hoặc sửa lỗi
  - Ví dụ: `feature/multiplication-division`, `feature/exponentiation`
  
- **Commits**: Commit thường xuyên với mô tả rõ ràng
  
- **Pull Request (PR)**: Đẩy nhánh lên GitHub và tạo PR để Code Review
  
- **Merge**: Gộp nhánh vào `main` sau khi kiểm tra kỹ lưỡng

---

## 3. Bảo mật GitHub

### Các điều cần tuân thủ

- **Không lưu thông tin nhạy cảm**
  - Tuyệt đối không commit: API Keys, mật khẩu, file `.env`
  
- **Sử dụng `.gitignore`**
  - Khai báo các file không cần track: `node_modules/`, `__pycache__/`, build artifacts
  
- **Sử dụng GitHub Secrets**
  - Khi tích hợp CI/CD (GitHub Actions), lưu biến môi trường tại Settings > Secrets and Variables

---

## 4. Thực hành Pull Request

Các Pull Request đã thực hiện thành công:

| PR | Mô tả | Nhánh |
|----|----|-------|
| #1 | Add multiplication and division methods | `feature/multiplication-division` → `main` |
| #2 | Add exponentiation and documentation | `feature/exponentiation` → `main` |

---

## 5. Xử lý Conflict

### Tình huống
Nhánh `main` và nhánh tính năng cùng chỉnh sửa các dòng code giống nhau → Xung đột (Conflict)

### Cách giải quyết
1. Sử dụng editor để giữ lại code mong muốn
2. Xóa các thẻ đánh dấu: `<<<<<<<`, `=======`, `>>>>>>>`
3. Commit merge hoàn tất quy trình

**Ví dụ conflict markers:**
```
# Code từ nhánh khác
```

---

## 6. Revert an toàn

### Tình huống
Cần hoàn tác một commit lỗi mà không làm mất lịch sử

### Giải pháp
```bash
git revert <commit-id>
```

**Lợi ích:**
- Tạo commit mới đảo ngược thay đổi
- Giữ lại lịch sử commit rõ ràng
- An toàn hơn so với `git reset --hard`

---

## 7. Vibe Coding với AI

Khi làm việc với các công cụ AI (ChatGPT, Gemini, Copilot, GitHub Copilot):

### Best Practices

- **Tạo nhánh tính năng nhỏ**
  - Tránh để AI viết đè trực tiếp lên `main`
  
- **Review code chặt chẽ**
  - AI có thể tạo lỗi hoặc lỗ hổng bảo mật
  - Luôn tạo PR và kiểm thử trước khi merge
  
- **Commit theo từng bước nhỏ**
  - Dễ phát hiện code AI bị lỗi
  - Dễ revert nếu cần thiết
  
- **Kiểm tra bảo mật**
  - Đảm bảo AI không tự động thêm API keys, credentials vào code

---

## 📝 Ghi chú

- Mỗi commit nên có mô tả ý nghĩa
- Pull Request cần được review trước merge
- Luôn giữ `main` ở trạng thái hoạt động
- Backup thường xuyên trên remote (GitHub)
