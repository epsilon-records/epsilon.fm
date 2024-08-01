<script lang="ts">
	import ToggleLayoutOptions from '$lib/components/ToggleLayoutOptions.svelte';
	import QuickNavigate from '$lib/components/QuickNavigate.svelte';
	import ToggleFullScreen from '$lib/components/ToggleFullScreen.svelte';
	import * as Menubar from '$lib/components/ui/menubar/index';
	import { goto } from '$app/navigation';
	import { waveformBarVisible, sidebarVisible, statusBarVisible } from '$lib/stores/ui';
	import QuickNavigateSettings from '$lib/components/QuickNavigateSettings.svelte';

	const items = ['dashboard', 'music', 'orders', 'products', 'customers', 'analytics'];

	let isFullScreen = false;

	function toggleFullScreen() {
		if (!document.fullscreenElement) {
			document.documentElement.requestFullscreen();
			isFullScreen = true;
		} else {
			if (document.exitFullscreen) {
				document.exitFullscreen();
				isFullScreen = false;
			}
		}
	}

	function handleKeydown(event: KeyboardEvent) {
		if (!event.metaKey) return;
		if (event.key === 'f') {
			event.preventDefault();
			toggleFullScreen();
		} else if (event.key === 'e') {
			event.preventDefault();
			waveformBarVisible.update((value) => !value);
		} else if (event.key === '/') {
			event.preventDefault();
			statusBarVisible.update((value) => !value);
		} else if (event.key === '\\') {
			event.preventDefault();
			sidebarVisible.update((value) => !value);
		} else {
			const key = parseInt(event.key);
			if (!isNaN(key) && key > 0 && key <= items.length) {
				event.preventDefault();
				goto(`/${items[key - 1]}`);
			}
		}
	}
</script>

<svelte:window on:keydown={handleKeydown} />

<Menubar.Menu>
	<Menubar.Trigger>View</Menubar.Trigger>
	<Menubar.Content>
		<QuickNavigate />
		<Menubar.Separator />
		<QuickNavigateSettings />
		<Menubar.Separator />
		<ToggleLayoutOptions />
		<Menubar.Separator />
		<ToggleFullScreen />
	</Menubar.Content>
</Menubar.Menu>
