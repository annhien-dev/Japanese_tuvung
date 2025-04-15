import streamlit as st
from gtts import gTTS
import tempfile

# Cấu hình ứng dụng
st.set_page_config(page_title="Học từ vựng tiếng Nhật", layout="centered")

# Từ vựng và câu hỏi quiz
word = {
    "tuvung": "地位（ちい）",
    "nghia": "địa vị, vị trí xã hội",
    "vidu": "彼は会社で高い地位にある。",
    "vidu_vn": "Anh ấy có địa vị cao trong công ty。",
    "quiz": [
        {
            "cauhoi": "『地位』 có nghĩa là gì?",
            "luachon": ["lời khuyên", "địa vị, vị trí xã hội", "sự giúp đỡ"],
            "dapan": "địa vị, vị trí xã hội"
        },
        {
            "cauhoi": "Câu nào dùng đúng từ 『地位』?",
            "luachon": [
                "彼は会社で高い地位にある。",
                "彼は忠告を聞かなかった。",
                "地位を敬意で払う。"
            ],
            "dapan": "彼は会社で高い地位にある。"
        },
        {
            "cauhoi": "Điền vào chỗ trống: 彼は会社で高い（　）にある。",
            "luachon": ["忠告", "地位", "苦痛"],
            "dapan": "地位"
        }
    ]
}

# Hiển thị từ vựng
st.title("📘 Học từ vựng: 地位（ちい）")
st.subheader(f"Từ vựng: {word['tuvung']}")
st.write(f"**Nghĩa:** {word['nghia']}")
st.write(f"**Ví dụ:** {word['vidu']}")
st.caption(f"{word['vidu_vn']}")

# Tạo âm thanh phát âm từ gTTS
tts = gTTS(word["tuvung"], lang='ja')
with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
    tts.save(fp.name)
    st.audio(fp.name)

# Trắc nghiệm
st.markdown("---")
st.subheader("📝 Trắc nghiệm")

for idx, q in enumerate(word["quiz"]):
    st.write(f"**Câu {idx+1}: {q['cauhoi']}**")
    ans = st.radio("Chọn đáp án", q["luachon"], key=idx)
    if st.button(f"Kiểm tra câu {idx+1}", key=f"btn{idx}"):
        if ans == q["dapan"]:
            st.success("✅ Chính xác!")
        else:
            st.error(f"❌ Sai rồi. Đáp án đúng là: {q['dapan']}")
    st.markdown("---")
