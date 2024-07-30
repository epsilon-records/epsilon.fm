<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar';
</script>

<Menubar.Item
	on:click={() =>
		document.fullscreenElement
			? document.exitFullscreen()
			: document.documentElement.requestFullscreen()}
	inset
	>{document.fullscreenElement ? 'Exit Full Screen' : 'Enter Full Screen'}<Menubar.Shortcut
		>⌘F</Menubar.Shortcut
	></Menubar.Item
>
