import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class ResInformation extends StatelessWidget {
@override
  Widget build(BuildContext context) {
    return Column(
        children: [
            Container(
                width: 390,
                height: 844,
                clipBehavior: Clip.antiAlias,
                decoration: ShapeDecoration(
                color: Colors.white,
                shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(46),
                ),
            ),
child: Stack(
children: [
Positioned(
left: 318,
top: 293,
child: Container(
width: 50,
height: 50,
padding: const EdgeInsets.all(18),
decoration: ShapeDecoration(
color: Color(0xFFEFF2F5),
shape: RoundedRectangleBorder(
borderRadius: BorderRadius.circular(100),
),
),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 22,
height: 22,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 22,
height: 22,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
),
Positioned(
left: 26,
top: 286,
child: Container(
width: 201,
height: 63,
child: Stack(
children: [
Positioned(
left: 1,
top: 0,
child: Text(
'오양칼국수',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 36,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 42,
letterSpacing: -1.80,
),
),
),
Positioned(
left: 23,
top: 43,
child: Text(
'충남 보령시 보령남로 125-7',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 16,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
Positioned(
left: 0,
top: 44,
child: Container(
width: 19,
height: 19,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 19,
height: 19,
child: Stack(children: [
,
]),
),
],
),
),
),
],
),
),
),
Positioned(
left: -25,
top: 476,
child: Container(
width: 419,
height: 59,
child: Stack(
children: [
Positioned(
left: 22,
top: 0,
child: Container(
width: 396,
height: 59,
decoration: BoxDecoration(color: Color(0xFFEFF2F5)),
),
),
Positioned(
left: 170,
top: 18,
child: Text(
'식사 메뉴',
textAlign: TextAlign.center,
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 17,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 21,
letterSpacing: -0.17,
),
),
),
Positioned(
left: 0,
top: 18,
child: Text(
'Breakfast Menu',
style: TextStyle(
color: Color(0xFFB3BFCB),
fontSize: 17,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 21,
letterSpacing: -0.17,
),
),
),
Positioned(
left: 288,
top: 18,
child: Text(
'Overnight Menu',
style: TextStyle(
color: Color(0xFFB3BFCB),
fontSize: 17,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 21,
letterSpacing: -0.17,
),
),
),
Positioned(
left: 140,
top: 56,
child: Container(
width: 126,
height: 3,
decoration: BoxDecoration(color: Color(0xFFFFC95F)),
),
),
],
),
),
),
Positioned(
left: 21,
top: 373,
child: Container(
width: 348,
height: 79,
child: Stack(
children: [
Positioned(
left: 15,
top: 15,
child: Container(
width: 20,
height: 20,
decoration: ShapeDecoration(
color: Color(0xFF292D32),
shape: StarBorder(
points: 5,
innerRadiusRatio: 0.49,
pointRounding: 1.50,
valleyRounding: 0,
rotation: 0,
squash: 0,
),
),
),
),
Positioned(
left: 42,
top: 19,
child: Text(
'십시일반 포인트 17950원',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 15,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
),
),
),
Positioned(
left: 42,
top: 48,
child: Text(
'매일 09:00 ~ 19:00',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 15,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
),
),
),
Positioned(
left: 0,
top: 0,
child: Opacity(
opacity: 0.30,
child: Container(
width: 348,
height: 79,
decoration: ShapeDecoration(
color: Color(0xFFB3BFCB),
shape: RoundedRectangleBorder(
borderRadius: BorderRadius.circular(10),
),
),
),
),
),
Positioned(
left: 284,
top: 15,
child: Container(
width: 50,
height: 50,
child: Stack(
children: [
Positioned(
left: 0,
top: 0,
child: Container(
width: 50,
height: 50,
decoration: ShapeDecoration(
color: Colors.white,
shape: OvalBorder(),
),
),
),
Positioned(
left: 14,
top: 13,
child: Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
),
],
),
),
),
],
),
),
),
Positioned(
left: 0,
top: 831,
child: Container(
height: 99,
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
width: double.infinity,
padding: const EdgeInsets.only(
top: 16,
left: 21,
right: 21,
bottom: 18,
),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 108,
padding: const EdgeInsets.only(top: 5, bottom: 6),
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.end,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 117,
height: 26,
decoration: BoxDecoration(
image: DecorationImage(
image: NetworkImage("https://via.placeholder.com/117x26"),
fit: BoxFit.cover,
),
),
),
],
),
),
const SizedBox(width: 10),
Expanded(
child: Container(
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
SizedBox(
width: double.infinity,
child: Text(
'Veggie & Bacon Hot Sauce Sandwich ',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 17,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 23,
letterSpacing: -0.17,
),
),
),
const SizedBox(height: 1),
Container(
width: double.infinity,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Text(
'\$6.89',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 16,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
textDecoration: TextDecoration.lineThrough,
height: 18,
),
),
const SizedBox(width: 9),
Text(
'\$5.59',
style: TextStyle(
color: Color(0xFF45B7E8),
fontSize: 16,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 18,
),
),
],
),
),
],
),
),
),
const SizedBox(width: 10),
Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
],
),
),
),
Positioned(
left: 0,
top: 938,
child: Container(
height: 122,
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
width: double.infinity,
padding: const EdgeInsets.only(
top: 16,
left: 21,
right: 21,
bottom: 18,
),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
padding: const EdgeInsets.only(left: 11),
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.end,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 109,
height: 40,
decoration: BoxDecoration(
image: DecorationImage(
image: NetworkImage("https://via.placeholder.com/109x40"),
fit: BoxFit.cover,
),
),
),
],
),
),
const SizedBox(width: 10),
Expanded(
child: Container(
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
SizedBox(
width: double.infinity,
child: Text(
'Western BBQ Cheeseburger (400 Cals)',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 17,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 23,
letterSpacing: -0.17,
),
),
),
const SizedBox(height: 1),
Container(
width: double.infinity,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Text(
'\$5.89',
style: TextStyle(
color: Color(0xFF292D32),
fontSize: 16,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
textDecoration: TextDecoration.lineThrough,
height: 18,
),
),
const SizedBox(width: 9),
Text(
'\$4.59',
style: TextStyle(
color: Color(0xFF45B7E8),
fontSize: 16,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
height: 18,
),
),
],
),
),
],
),
),
),
const SizedBox(width: 10),
Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
],
),
),
),
Positioned(
left: 0,
top: 0,
child: Container(
width: 390,
height: 86,
child: Stack(
children: [
Positioned(
left: 0,
top: 0,
child: Container(
width: 390,
height: 86,
decoration: BoxDecoration(color: Color(0xFFFFC95F)),
),
),
Positioned(
left: 0,
top: -1,
child: Container(
width: 372.14,
height: 44,
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Stack(
children: [
Positioned(
left: 0,
top: 0,
child: Container(
width: 372,
height: 30,
child: Stack(children: [
,
]),
),
),
Positioned(
left: 289,
top: 16,
child: Container(
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 20,
height: 14,
child: Stack(children: [
,
]),
),
const SizedBox(width: 4),
Container(
width: 16,
height: 14,
padding: const EdgeInsets.only(
top: 2,
left: 1,
right: 0.75,
bottom: 2,
),
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
,
],
),
),
const SizedBox(width: 4),
Container(
width: 25,
height: 14,
child: Stack(
children: [
Positioned(
left: 2,
top: 3,
child: Container(
width: 19,
height: 8,
decoration: ShapeDecoration(
color: Colors.black,
shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(1)),
),
),
),
],
),
),
],
),
),
),
Positioned(
left: 295,
top: 8,
child: Container(
width: 6,
height: 6,
child: Stack(children: [
,
]),
),
),
Positioned(
left: 21,
top: 12,
child: Container(
width: 54,
height: 21,
padding: const EdgeInsets.only(top: 3, left: 11, right: 10, bottom: 3),
clipBehavior: Clip.antiAlias,
decoration: ShapeDecoration(
shape: RoundedRectangleBorder(
borderRadius: BorderRadius.circular(20),
),
),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 33,
height: 15,
padding: const EdgeInsets.only(
top: 2,
left: 2,
right: 2.57,
bottom: 1.91,
),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
,
],
),
),
],
),
),
),
],
),
),
),
Positioned(
left: 152.82,
top: 43,
child: Text(
'가게정보',
textAlign: TextAlign.center,
style: TextStyle(
color: Colors.black,
fontSize: 24,
fontFamily: 'GyeonggiTitleB',
fontWeight: FontWeight.w700,
),
),
),
],
),
),
),
Positioned(
left: 0,
top: 86,
child: Container(
width: 390,
height: 176,
decoration: BoxDecoration(
image: DecorationImage(
image: NetworkImage("https://via.placeholder.com/390x176"),
fit: BoxFit.fill,
),
),
),
),
Positioned(
left: 0,
top: 550,
child: Container(
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
height: 71.63,
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
width: 349,
padding: const EdgeInsets.only(top: 10),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
SizedBox(
width: 302,
height: 27,
child: Text(
'오.칼 (보리밥)',
style: TextStyle(
color: Colors.black,
fontSize: 20,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
const SizedBox(width: 23),
SizedBox(
width: 302,
height: 34.63,
child: Text(
'9000원',
style: TextStyle(
color: Color(0xFFFF5B00),
fontSize: 16,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
],
),
),
const SizedBox(height: 10),
Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
],
),
),
const SizedBox(height: 5),
Container(
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
height: 71.63,
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
width: 349,
padding: const EdgeInsets.only(top: 10),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
SizedBox(
width: 302,
height: 27,
child: Text(
'키.칼 (보리밥)',
style: TextStyle(
color: Colors.black,
fontSize: 20,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
const SizedBox(width: 23),
SizedBox(
width: 302,
height: 34.63,
child: Text(
'8000원',
style: TextStyle(
color: Color(0xFFFF5B00),
fontSize: 16,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
],
),
),
const SizedBox(height: 10),
Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
],
),
),
const SizedBox(height: 5),
Container(
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
height: 71.63,
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
width: 349,
padding: const EdgeInsets.only(top: 10),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
SizedBox(
width: 302,
height: 27,
child: Text(
'오.키칼 (보리밥)',
style: TextStyle(
color: Colors.black,
fontSize: 20,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
const SizedBox(width: 23),
SizedBox(
width: 302,
height: 34.63,
child: Text(
'10000원',
style: TextStyle(
color: Color(0xFFFF5B00),
fontSize: 16,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
],
),
),
const SizedBox(height: 10),
Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
],
),
),
const SizedBox(height: 5),
Container(
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
height: 71.63,
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
width: 349,
padding: const EdgeInsets.only(top: 10),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
SizedBox(
width: 302,
height: 27,
child: Text(
'키.칼 (보리밥)',
style: TextStyle(
color: Colors.black,
fontSize: 20,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
const SizedBox(width: 23),
SizedBox(
width: 302,
height: 34.63,
child: Text(
'8000원',
style: TextStyle(
color: Color(0xFFFF5B00),
fontSize: 16,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
],
),
),
const SizedBox(height: 10),
Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
],
),
),
const SizedBox(height: 5),
Container(
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(),
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.start,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
height: 71.63,
child: Column(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
Container(
width: 349,
padding: const EdgeInsets.only(top: 10),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.start,
children: [
SizedBox(
width: 302,
height: 27,
child: Text(
'키.칼 (보리밥)',
style: TextStyle(
color: Colors.black,
fontSize: 20,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
const SizedBox(width: 23),
SizedBox(
width: 302,
height: 34.63,
child: Text(
'8000원',
style: TextStyle(
color: Color(0xFFFF5B00),
fontSize: 16,
fontFamily: 'Pretendard',
fontWeight: FontWeight.w400,
),
),
),
],
),
),
const SizedBox(height: 10),
Container(
width: 24,
height: 24,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 24,
height: 24,
child: Stack(children: [
,
]),
),
],
),
),
],
),
),
],
),
),
],
),
),
),
Positioned(
left: 10,
top: 802,
child: Container(
width: 375,
height: 42,
padding: const EdgeInsets.only(
top: 29,
left: 120,
right: 121,
bottom: 8,
),
clipBehavior: Clip.antiAlias,
decoration: BoxDecoration(
color: Colors.white.withOpacity(0.8999999761581421),
),
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 134,
height: 5,
child: Row(
mainAxisSize: MainAxisSize.min,
mainAxisAlignment: MainAxisAlignment.center,
crossAxisAlignment: CrossAxisAlignment.center,
children: [
Container(
width: 134,
height: 5,
decoration: ShapeDecoration(
color: Colors.black,
shape: RoundedRectangleBorder(
borderRadius: BorderRadius.circular(10),
),
),
),
],
),
),
],
),
),
),
],
),
),
],
);
}
}