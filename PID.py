from models import ObjectWithInertia, PIDController, init_plot, add_to_plot, signal_to_force, finalize_plot

# Создаем объект с массой 10 кг.
object_with_inertia = ObjectWithInertia(mass=10, friction_coefficient=7)

# Рассчитываем коэффициенты регулятора по методу Зиглера-Никольса
# Частота устойчивых колебаний: 25.85
# Период колебаний T: 2
# Значит kp = 0.4 * 25.85 = 10.34
# ki = (1.2 * 10.34)/2 = 6.204
regulator = PIDController(kp=10.34, ki=6.204, kd=0., increment_mode=False)

time_points = []  # Время (с)
velocity_points = []  # Скорость (м/с)
control_signals = []  # Управляющий сигнал


targets = [5.0] * 20 + [7.0] * 30 + [3.0] * 30
force = 0
for current_time in range(80):
    velocity = object_with_inertia.apply_force(force, current_time)
    control_signal = regulator.apply_regulation(velocity, targets[current_time])
    force = signal_to_force(control_signal)

    print(f"Time: {current_time:.2f} s, Error: {regulator.error:.2f}, Signal: {control_signal:.2f}, Force: {force:.2f}, Velocity: {velocity:.2f} m/s")
    time_points.append(current_time)
    velocity_points.append(velocity)
    control_signals.append(control_signal)

init_plot()
add_to_plot(time_points, velocity_points, "Время (с)", "Скорость (м/с)", "График скорости от времени")
finalize_plot()
# init_plot()
# add_to_plot(time_points, control_signals, "Время (с)", "Управляющий сигнал", "")
# finalize_plot()