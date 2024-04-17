import mysql.connector

# 데이터베이스 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="LittleLemon"
)

cursor = conn.cursor()

# 데이터 삽입
def add_booking(name, date, guests):
    sql = "INSERT INTO Bookings (CustomerName, BookingDate, NumberOfGuests) VALUES (%s, %s, %s)"
    values = (name, date, guests)
    cursor.execute(sql, values)
    conn.commit()

# 예약 취소
def cancel_booking(booking_id):
    sql = "DELETE FROM Bookings WHERE BookingID = %s"
    cursor.execute(sql, (booking_id,))
    conn.commit()

# 예약 업데이트
def update_booking(booking_id, guests):
    sql = "UPDATE Bookings SET NumberOfGuests = %s WHERE BookingID = %s"
    cursor.execute(sql, (guests, booking_id))
    conn.commit()

# 데이터 조회
def get_max_quantity():
    sql = "SELECT MAX(NumberOfGuests) FROM Bookings"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]

# 필요한 함수 호출 예시
add_booking('Alice Smith', '2022-10-01', 4)
cancel_booking(1)
update_booking(2, 5)
print(get_max_quantity())

# 연결 종료
cursor.close()
conn.close()
