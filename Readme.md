# Kernbalance

Historical Python data logger for Kern laboratory balances.

I wrote this during Mars simulation chamber work to automatically log evaporation-driven mass loss from Mars simulant soils under vacuum. The script communicates with a Kern balance over RS-232/serial, samples mass over time, averages measurements, stores NumPy arrays, and can export/plot the resulting data.

This is an old research utility, preserved as a small example of scientific automation and hardware/data acquisition.

## Context

The experiment measured mass change over time while soil samples were exposed to low-pressure chamber conditions. Manual logging was impractical, so the balance was queried automatically and the data was saved for later analysis.

## Features

- Serial communication with Kern balance
- Configurable sampling rate
- Averaging to reduce noise and file size
- NumPy `.npy` storage
- CSV/text export
- Simple plotting of mass vs. time

## Notes

This code is historical and was written for a specific Windows/Python 2 lab setup. It is not maintained as a modern package.