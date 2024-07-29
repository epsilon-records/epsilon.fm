<script lang="ts">
	import MusicTabs from '$lib/components/MusicTabs.svelte';
	import { playlists } from '$lib/components/(data)/playlists.js';
	import Menu from '$lib/components/Menu.svelte';
	import Sidebar from '$lib/components/Sidebar.svelte';
</script>

<Menu />
<div class="border-t bg-background">
	<div class="grid lg:grid-cols-5">
		<Sidebar {playlists} class="hidden lg:block" />
		<div class="col-span-3 lg:col-span-4 lg:border-l">
			<div class="h-full px-4 py-6 lg:px-8">
				<MusicTabs></MusicTabs>
			</div>
		</div>
	</div>
</div>
