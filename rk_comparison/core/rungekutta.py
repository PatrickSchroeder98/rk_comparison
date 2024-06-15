class rungekutta:
    """This class contains Runge-Kutta methods of orders from 1 to 6."""

    def rungekutta1(self, f, x, y1, n, h):
        """Runge-Kutta order 1, known as Euler's method. Sources: [1], [2] in in bibliography"""
        for i in range(n):
            k1 = h * f(x[i], y1[i])

            x.append(x[i] + h)
            y1.append(y1[i] + k1)

    def rungekutta2(self, f, x, y1, n, h):
        """Runge-Kutta order 2, sources: [1], [2] in in bibliography"""
        for i in range(n):
            k1 = h * f(x[i], y1[i])
            k2 = h * f(x[i] + (2.0 / 3.0) * h, y1[i] + (2.0 / 3.0) * k1)

            x.append(x[i] + h)
            y1.append(y1[i] + (0.25 * k1) + (0.75 * k2))

    def RungeKutta3(self, f, x, y1, n, h):
        """Runge-Kutta order 3, sources: [1], [2] in in bibliography"""
        for i in range(n):
            k1 = h * f(x[i], y1[i])
            k2 = h * f(x[i] + 0.5 * h, y1[i] + 0.5 * k1)
            k3 = h * f(x[i] + 0.75 * h, y1[i] + 0.75 * k2)

            x.append(x[i] + h)
            y1.append(
                y1[i] + ((2.0 / 9.0) * k1) + ((1.0 / 3.0) * k2) + ((4.0 / 9.0) * k3)
            )

    def RungeKutta4(self, f, x, y1, n, h):
        """Runge-Kutta order 3, sources: [1], [2] in in bibliography"""
        for i in range(n):
            k1 = h * f(x[i], y1[i])
            k2 = h * f(x[i] + 0.5 * h, y1[i] + 0.5 * k1)
            k3 = h * f(x[i] + 0.5 * h, y1[i] + 0.5 * k2)
            k4 = h * f(x[i] + h, y1[i] + k3)

            x.append(x[i] + h)
            y1.append(y1[i] + (1.0 / 6.0) * (k1 + (2.0 * k2) + (2.0 * k3) + k4))

    def RungeKutta5(self, f, x, y1, n, h):
        """Runge-Kutta order 5, source: [1], [3] in bibliography"""
        for i in range(n):
            k1 = h * f(x[i], y1[i])
            k2 = h * f(x[i] + 0.25 * h, y1[i] + 0.25 * k1)
            k3 = h * f(x[i] + 0.25 * h, y1[i] + 0.125 * k1 + 0.125 * k2)
            k4 = h * f(x[i] + 0.5 * h, y1[i] - 0.5 * k2 + k3)
            k5 = h * f(x[i] + 0.75 * h, y1[i] + 0.1875 * k1 + 0.5625 * k4)
            k6 = h * f(
                x[i] + h,
                y1[i]
                - (3.0 / 7.0) * k1
                + (2.0 / 7.0) * k2
                + (12.0 / 7.0) * k3
                - (12.0 / 7.0) * k4
                + (8.0 / 7.0) * k5,
            )

            x.append(x[i] + h)
            y1.append(
                y1[i]
                + (1.0 / 90.0)
                * (7.0 * k1 + 32.0 * k2 + 12.0 * k4 + 32.0 * k5 + 7.0 * k6)
            )

    def RungeKutta6(self, f, x, y1, n, h):
        """Runge-Kutta order 6, source: [1], [4] in bibliography"""
        for i in range(n):
            k1 = h * f(x[i], y1[i])
            k2 = h * f(x[i] + (1.0 / 9.0) * h, y1[i] + (1.0 / 9.0) * k1)
            k3 = h * f(x[i] + (1.0 / 6.0) * h, y1[i] + (1.0 / 24.0) * (k1 + k2))
            k4 = h * f(
                x[i] + (1.0 / 3.0) * h, y1[i] + (1.0 / 6.0) * (k1 - 3.0 * k2 + 4.0 * k3)
            )
            k5 = h * f(x[i] + (1.0 / 2.0) * h, y1[i] + (1.0 / 8.0) * (k1 + 3 * k4))
            k6 = h * f(
                x[i] + (2.0 / 3.0) * h,
                y1[i]
                + (1.0 / 3.0)
                * (-4.0 * k1 - 21.0 * k2 + 46.0 * k3 - 29.0 * k4 + 10.0 * k5),
            )
            k7 = h * f(
                x[i] + (5.0 / 6.0) * h,
                y1[i]
                + (1.0 / 72.0)
                * (-8.0 * k1 + 99.0 * k2 - 84.0 * k3 + 44.0 * k5 + 9.0 * k6),
            )
            k8 = h * f(
                x[i] + h,
                y1[i]
                + (1.0 / 82.0)
                * (
                    107.0 * k1
                    - 234.0 * k2
                    + 354.0 * k4
                    - 172.0 * k5
                    - 36.0 * k6
                    + 72.0 * k7
                ),
            )

            x.append(x[i] + h)
            y1.append(
                y1[i]
                + (1.0 / 840.0)
                * (41.0 * (k1 + k8) + 216.0 * (k3 + k7) + 27.0 * (k4 + k6) + 272.0 * k5)
            )
