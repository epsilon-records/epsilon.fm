<script>
	import { onMount } from 'svelte';
	import { audioControlsReady } from '$lib/stores/audio';

	onMount(() => {
		audioControlsReady.set(true);
	});
</script>

<div id="audio-controls">
	<!-- the audio controls will be rendered here -->
</div>
