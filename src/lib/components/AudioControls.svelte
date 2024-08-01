<script>
	import { onMount } from 'svelte';
	import { audioControlsReady } from '$lib/stores/ui';

	onMount(() => {
		audioControlsReady.set(true);
	});
</script>

<div id="audio-controls">
	<!-- the audio controls will be rendered here -->
</div>
