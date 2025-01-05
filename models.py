import math
import matplotlib.pyplot as plt
import random

def init_plot():
    # Инициализация графика
    plt.figure(figsize=(10, 6))  # Размер графика

def add_to_plot(x_points, y_points, xlabel, ylabel, title):
    # Построение графика
    plt.plot(x_points, y_points, label=ylabel)

    # Добавление осей и заголовка
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


def finalize_plot():
    # Сетка и легенда
    plt.grid(True)
    plt.legend()

    # Отображение графика
    plt.show()

class ObjectWithInertia:
    def __init__(self, mass, friction_coefficient, initial_velocity=0.0):
        """
        Инициализация объекта с инерцией.
        :param mass: Масса объекта (кг).
        :param friction_coefficient: Коэффициент трения (Н/м/с).
        :param initial_velocity: Начальная скорость объекта (м/с).
        """
        self.mass = mass
        self.velocity = initial_velocity
        self.friction_coefficient = friction_coefficient
        self.last_time = None  # Последний момент времени, когда вычислялась скорость.

    def apply_force(self, force, current_time):
        """
        Применяет силу к объекту и возвращает его текущую скорость.
        :param force: Прикладываемая сила (Н).
        :param current_time: Текущий момент времени (с).
        :return: Текущая скорость объекта (м/с).
        """
        if self.last_time is None:
            # Если функция вызывается впервые, сохраняем текущий момент времени.
            self.last_time = current_time
            return self.velocity

        # Вычисляем разницу во времени.
        delta_time = current_time - self.last_time

        # Уравнение движения: F = ma -> a = (F - F_friction) / m
        # Сила трения: F_friction = -friction_coefficient * velocity
        friction_force = -self.friction_coefficient * self.velocity
        total_force = force + friction_force
        acceleration = total_force / self.mass

        # Изменение скорости: v = v0 + a * Δt
        self.velocity += acceleration * delta_time

        # Обновляем последний момент времени.
        self.last_time = current_time

        return self.velocity
    

class PIDController:
    def __init__(self, kp=0.9, ki=0.0, kd=0.0, increment_mode=False):
        self.Kp = kp # Пропорциональный коэффициент
        self.Ki = ki # Интегральный коэффициент
        self.Kd = kd
        self.out_signal = 0.0
        self.increment_mode = increment_mode
        self.integral_error = 0.0
        self.derivative_error = 0.0
        self.last_error = 0.0

    def apply_regulation(self, current_x, target_x):
        self.error = target_x - current_x

        if self.increment_mode:
            self.out_signal += self.Kp * self.error + self.Ki * self.integral_error + self.Kd * self.derivative_error
        else:
            self.out_signal = self.Kp * self.error + self.Ki * self.integral_error + self.Kd * self.derivative_error

        self.integral_error += self.error
        self.derivative_error = self.error - self.last_error
        self.last_error = self.error

        return self.out_signal


def signal_to_force(signal):
    if signal < 0.5:
        return 0.1
    elif signal > 0.5 and signal < 2.0:
        return 0.35 * signal
    elif signal > 2.0 and signal < 5.0:
        return 1.0 * signal
    elif signal > 5.0 and signal < 7.0:
        return 0.75 * signal
    else:
        return 0.6 * signal

# def signal_to_force(signal):
#     noise = random.uniform(-0.1, 0.1)
#     return 20 / (1 + math.exp(-signal/20))