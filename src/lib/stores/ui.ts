import { writable } from 'svelte/store';

export const statusBarVisible = writable(true);
export const sidebarVisible = writable(true);
export const waveformBarVisible = writable(true);
export const audioControlsReady = writable(false);
export const militaryTimeEnabled = writable(true);
