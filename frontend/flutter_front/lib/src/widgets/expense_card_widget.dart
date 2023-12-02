import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class ExpenseCard extends StatelessWidget {
  final String category = 'Food';
  final double amount = 12.32;
  final DateTime time = DateTime.now();
  final String comments = 'This is a comment';

  // // Constructor to initialize the fields
  // ExpenseCard({
  //   required this.category,
  //   required this.amount,
  //   required this.time,
  //   this.comments = '', // Optional comments with a default empty string
  // });

  @override
  Widget build(BuildContext context) {
    return Card(
      color: Colors.white,
      elevation: 4.0,
      margin: const EdgeInsets.all(8.0),
      child: ListTile(
        leading: const Icon(
          Icons.category,
          size: 30,
          color: Colors.blue,
        ),
        title: Text(
          category,
          style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
        ),
        subtitle: Text(
          '${NumberFormat.currency(symbol: "\$").format(amount)}\n${DateFormat.yMMMd().add_jm().format(time)}\n$comments',
          style: TextStyle(color: Colors.grey[600]),
        ),
        isThreeLine: true,
      ),
    );
  }
}
