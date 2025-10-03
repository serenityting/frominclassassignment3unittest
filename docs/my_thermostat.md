::: example_functions.my_thermo_stat

Based on current and preferred temperature,
    determine status of heat,cool and stay off

    Args:
        temp: current temperature
        desired_temp: preferred temperature

    Returns:
        String printing 'Heat','AC' or 'off'