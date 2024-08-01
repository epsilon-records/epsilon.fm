<script lang="ts">
	import WaveSurfer from 'wavesurfer.js';
	import { onMount } from 'svelte';
	import vozzRich from '$lib/audio/vozz-rich.mp3';
	import { sidebarVisible } from '$lib/stores/ui';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import Hover from 'wavesurfer.js/dist/plugins/hover.esm.js';

	let wavesurfer: WaveSurfer;

	onMount(() => {
		const audio = new Audio();
		audio.controls = true;
		audio.src = vozzRich;
		audio.className = 'p-0';
		wavesurfer = WaveSurfer.create({
			container: '#waveform',
			waveColor: 'rgb(200, 0, 200)',
			progressColor: 'rgb(100, 0, 100)',
			media: audio,
			barWidth: 2,
			barGap: 1,
			barRadius: 2,
			plugins: [
				Hover.create({
					lineColor: '#ff0000',
					lineWidth: 2,
					labelBackground: '#555',
					labelColor: '#fff',
					labelSize: '11px'
				})
			]
		});
		const audioControls = document.querySelector('#audio-controls');
		if (audioControls) {
			audio.className = 'h-6';
			audioControls.appendChild(audio);
		}

		wavesurfer.on('interaction', () => {
			wavesurfer.play();
		});

		return () => {
			if (audioControls) {
				audioControls.removeChild(audio);
			}
			wavesurfer.destroy();
		};
	});
</script>

<SignedIn>
	<div
		id="waveform"
		class="fixed bottom-0 left-0 w-full border-t bg-background class:pl-14={$sidebarVisible}"
	>
		<!-- the waveform will be rendered here -->
	</div>
</SignedIn>
