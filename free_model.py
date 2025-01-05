from models import ObjectWithInertia, PIDController, add_to_plot, finalize_plot

# Создаем объект с массой 10 кг.
object_with_inertia = ObjectWithInertia(mass=10, friction_coefficient=2)
regulator = PIDController()

time_points = []  # Время (с)
velocity_points = []  # Скорость (м/с)

for current_time in range(50):
    force = 20 if current_time < 20.0 else 0  # Сила действует первые 2 секунды.
    velocity = object_with_inertia.apply_force(force, current_time)
    print(f"Time: {current_time:.2f} s, Force: {force:.2f}, Velocity: {velocity:.2f} m/s")
    time_points.append(current_time)
    velocity_points.append(velocity)

add_to_plot(time_points, velocity_points, "Время (с)", "Скорость (м/с)", "График скорости от времени")
finalize_plot()