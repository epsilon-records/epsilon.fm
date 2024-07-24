export default {
	'**/*.{ts,js,svelte,css,html,json}': ['prettier --write --list-different', 'eslint'],
	'backend/**/*.py': [
		'poetry --directory ./backend run ruff check',
		'poetry --directory ./backend run ruff format'
	]
};
