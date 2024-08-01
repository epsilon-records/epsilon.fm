<script lang="ts">
	import SignIn from 'clerk-sveltekit/client/SignIn.svelte';
	import { mode } from 'mode-watcher';
	import { neobrutalism, dark } from '@clerk/themes';
	import { onMount, onDestroy } from 'svelte';
	import { statusBarVisible, waveformBarVisible } from '$lib/stores/ui';

	let originalStatusBarVisible: boolean;
	let originalWaveformBarVisible: boolean;

	onMount(() => {
		originalStatusBarVisible = $statusBarVisible;
		originalWaveformBarVisible = $waveformBarVisible;
		statusBarVisible.set(false);
		waveformBarVisible.set(false);
	});

	onDestroy(() => {
		statusBarVisible.set(originalStatusBarVisible);
		waveformBarVisible.set(originalWaveformBarVisible);
	});
</script>

<div class="m-4 flex flex-col items-center">
	<SignIn
		appearance={{ baseTheme: $mode === 'dark' ? dark : neobrutalism }}
		redirectUrl="/dashboard"
	/>
</div>
