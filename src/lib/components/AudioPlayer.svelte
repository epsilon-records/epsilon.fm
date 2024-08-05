<script lang="ts">
	import WaveSurfer from 'wavesurfer.js';
	import { onMount } from 'svelte';
	import vozzRich from '$lib/audio/vozz-rich.mp3';
	import { sidebarVisible, statusBarVisible, waveformBarVisible } from '$lib/stores/ui';
	import {} from '$lib/stores/audio';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import Hover from 'wavesurfer.js/dist/plugins/hover.esm.js';

	import { audioControlsReady, currentTrack, isPlaying } from '$lib/stores/audio';

	let wavesurfer: WaveSurfer;
	function loadTrack() {
		currentTrack.set({
			title: 'Never Stopping',
			artist: 'Vozz Rich'
		});
	}
	onMount(() => {
		const audio = new Audio();
		audio.controls = true;
		audio.src = vozzRich;
		audio.onplay = () => {
			isPlaying.set(true);
		};
		audio.onpause = () => {
			isPlaying.set(false);
		};
		loadTrack();
		wavesurfer = WaveSurfer.create({
			height: 64,
			autoCenter: true,
			container: '#waveform',
			waveColor: '#4A90E2',
			progressColor: '#666666',
			cursorColor: '#ff0000',
			media: audio,
			cursorWidth: 4,
			barWidth: 0,
			barGap: 0,
			barRadius: 0,
			barHeight: 0,
			plugins: [
				Hover.create({
					lineColor: '#dd5e98',
					lineWidth: 2,
					labelBackground: '#555',
					labelColor: '#fff',
					labelSize: '18px'
				})
			]
		});
		audioControlsReady.subscribe((ready) => {
			if (ready) {
				const audioControls = document.querySelector('#audio-controls');
				if (audioControls && audioControls.childNodes.length === 0) {
					audio.className = 'h-6';
					audioControls.appendChild(audio);
				}
			}
		});
		wavesurfer.on('interaction', () => {
			wavesurfer.play();
		});
	});
</script>

<div
	id="waveform"
	class="sticky z-50 mb-2 mt-4 h-16 border-t bg-background"
	class:hidden={!$waveformBarVisible}
	class:bottom-0={!$statusBarVisible}
	class:bottom-8={$statusBarVisible}
>
	<!-- the waveform will be rendered here -->
</div>
