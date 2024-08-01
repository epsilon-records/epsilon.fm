import { writable } from 'svelte/store';

export const audioControlsReady = writable(false);
export const currentTrack = writable({ title: '', artist: '' });
export const isPlaying = writable(false);
