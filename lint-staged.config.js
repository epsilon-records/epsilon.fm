export default {
	'**/*.{ts,js,svelte,css,html}': ['prettier --write --list-different', 'eslint --fix'],
	'backend/**/*.py': [
		'poetry --directory ./backend run ruff check --fix',
		'poetry --directory ./backend run ruff format'
	]
};
