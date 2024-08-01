<script lang="ts">
	import MenuSpacer from './MenuSpacer.svelte';
	import MenuHelp from './MenuHelp.svelte';
	import MenuAccount from './MenuAccount.svelte';
	import MenuEdit from './MenuEdit.svelte';
	import MenuFile from './MenuFile.svelte';
	import MenuAbout from './MenuAbout.svelte';
	import MenuView from './MenuView.svelte';
	import * as Menubar from '$lib/components/ui/menubar/index.js';
	import StarOnGitHub from './StarOnGitHub.svelte';
	import AudioControls from './AudioControls.svelte';

	import BrainQuickButton from './BrainQuickButton.svelte';
</script>

<Menubar.Root
	class="sticky top-0 z-50 flex items-center rounded-none border-b-4 border-none px-2 lg:px-4"
>
	<MenuAbout />
	<MenuFile />
	<MenuEdit />
	<MenuView />
	<MenuAccount />
	<MenuHelp />
	<MenuSpacer />
	<AudioControls />
	<MenuSpacer />
	<MenuSpacer />
	<BrainQuickButton />
	<!-- <StarOnGitHub /> -->
</Menubar.Root>
