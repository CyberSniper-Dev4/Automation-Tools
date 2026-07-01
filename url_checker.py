import requests

def check_url(url):
    """
    دالة لفحص حالة الرابط
    """
    # التأكد من أن الرابط يبدأ بـ http:// أو https://
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    
    try:
        print(f"جاري فحص الرابط: {url} ...")
        # إرسال طلب للرابط (بدون تحميل الصفحة كاملة لتوفير الوقت)
        response = requests.head(url, timeout=5)
        
        # التحقق من كود الحالة (Status Code)
        if response.status_code == 200:
            print(f"✅ الرابط يعمل بنجاح! (كود الحالة: {response.status_code})")
        else:
            print(f"⚠️ الرابط قد لا يعمل بشكل صحيح. (كود الحالة: {response.status_code})")
            
    except requests.ConnectionError:
        print("❌ فشل الاتصال. تأكد من الرابط ومن اتصالك بالإنترنت.")
    except requests.Timeout:
        print("⏳ انتهى وقت الاتصال. الرابط بطيء جداً أو لا يستجيب.")
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    print("=======================================")
    print("   مرحباً بك في أداة فحص الروابط (v1.0)   ")
    print("         برمجة: القناص السيبراني           ")
    print("=======================================")
    
    target_url = input("أدخل الرابط الذي تريد فحصه (مثال: google.com): ")
    if target_url:
        check_url(target_url)
    else:
        print("⚠️ لم يتم إدخال رابط.")

              
