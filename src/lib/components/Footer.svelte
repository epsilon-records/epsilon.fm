<script lang="ts">
	import StarOnGitHub from './StarOnGitHub.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
</script>

<footer>
	<slot name="footer">
		<MadeWithLove></MadeWithLove>
		<StarOnGitHub></StarOnGitHub>
	</slot>
</footer>
