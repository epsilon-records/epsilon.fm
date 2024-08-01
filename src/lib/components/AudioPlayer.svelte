<script lang="ts">
	import WaveSurfer from 'wavesurfer.js';
	import { onMount } from 'svelte';
	import vozzRich from '$lib/audio/vozz-rich.mp3';
	import {
		sidebarVisible,
		statusBarVisible,
		waveformBarVisible,
		audioControlsReady
	} from '$lib/stores/ui';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import Hover from 'wavesurfer.js/dist/plugins/hover.esm.js';

	let wavesurfer: WaveSurfer;

	onMount(() => {
		const audio = new Audio();
		audio.controls = true;
		audio.src = vozzRich;
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
		return () => {
			wavesurfer.destroy();
		};
	});
</script>

<SignedIn>
	<div
		id="waveform"
		class="fixed border-t bg-background"
		class:hidden={!$waveformBarVisible}
		class:w-full={!$sidebarVisible}
		class:w-[calc(100%-3.5rem)]={$sidebarVisible}
		class:left-0={!$sidebarVisible}
		class:left-14={$sidebarVisible}
		class:bottom-0={!$statusBarVisible}
		class:bottom-8={$statusBarVisible}
	>
		<!-- the waveform will be rendered here -->
	</div>
</SignedIn>
