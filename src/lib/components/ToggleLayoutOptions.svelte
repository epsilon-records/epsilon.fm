<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar';
	import { statusBarVisible, sidebarVisible, waveformBarVisible } from '$lib/stores/ui';
	function toggleSideBar() {
		sidebarVisible.update((value) => !value);
	}
	function toggleWaveformBar() {
		waveformBarVisible.update((value) => !value);
	}
	function toggleStatusBar() {
		statusBarVisible.update((value) => !value);
	}
</script>

<Menubar.CheckboxItem checked={$sidebarVisible} on:click={toggleSideBar}>
	{$sidebarVisible ? 'Hide' : 'Show'} Sidebar
	<Menubar.Shortcut>⌘\</Menubar.Shortcut>
</Menubar.CheckboxItem>
<Menubar.CheckboxItem checked={$waveformBarVisible} on:click={toggleWaveformBar}>
	{$waveformBarVisible ? 'Hide' : 'Show'} Waveform
	<Menubar.Shortcut>⌘E</Menubar.Shortcut>
</Menubar.CheckboxItem>
<Menubar.CheckboxItem checked={$statusBarVisible} on:click={toggleStatusBar}>
	{$statusBarVisible ? 'Hide' : 'Show'} Status Bar
	<Menubar.Shortcut>⌘/</Menubar.Shortcut>
</Menubar.CheckboxItem>
