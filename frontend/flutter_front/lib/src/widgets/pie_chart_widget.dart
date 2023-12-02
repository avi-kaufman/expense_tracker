import 'package:flutter/material.dart';
import 'package:pie_chart/pie_chart.dart';

class PieChartWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(50, 25, 25, 0),
      child: const PieChart(
        centerText: 'Monthly sepent\n 100\$',
        dataMap: {'Food': 3, 'Car': 8, 'Denis': 15},
        chartType: ChartType.ring,
        ringStrokeWidth: 15,
        colorList: [
          Color.fromARGB(255, 131, 212, 55),
          Color.fromRGBO(192, 192, 192, 1),
          Color.fromARGB(255, 50, 205, 200),
          Color.fromARGB(255, 51, 51, 51),
          Color.fromARGB(255, 154, 180, 70)
        ],
        chartValuesOptions: ChartValuesOptions(
          showChartValuesInPercentage: true,
        ),
        // totalValue: 50.0,
      ),
    );
  }
}
