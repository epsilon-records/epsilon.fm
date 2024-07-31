<script lang="ts">
	import WaveSurfer from 'wavesurfer.js';
	const wavesurfer = WaveSurfer.create({
		container: '#waveform',
		waveColor: '#4F4A85',
		progressColor: '#383351',
		url: '/audio.mp3'
	});

	wavesurfer.on('interaction', () => {
		wavesurfer.play();
	});
</script>

<div id="waveform">
	<!-- the waveform will be rendered here -->
</div>
