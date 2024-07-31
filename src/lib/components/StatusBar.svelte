<script lang="ts">
	import FavouritesMenu from './FavouritesMenu.svelte';
	import CurrentTime from './CurrentTime.svelte';
	import NetworkStatus from './NetworkStatus.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
	import { statusBarVisible, sideBarVisible } from '$lib/stores/ui';
</script>

{#if $statusBarVisible}
	<div class="status-bar fixed bottom-0 left-0 w-full border-t" class:pl-14={$sideBarVisible}>
		<div class="flex items-center justify-between px-1">
			<div class="flex items-center">
				<FavouritesMenu />
			</div>
			<div class="flex items-center">
				<MadeWithLove />
			</div>
			<div class="flex items-center space-x-1">
				<NetworkStatus />
				<CurrentTime />
			</div>
		</div>
	</div>
{/if}
