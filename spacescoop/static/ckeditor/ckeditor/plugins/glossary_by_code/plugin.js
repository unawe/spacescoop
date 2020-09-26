CKEDITOR.plugins.add( 'glossary', {
    icons: 'glossary',
    init: function( editor ) {

        editor.addCommand( 'glossary', new CKEDITOR.dialogCommand( 'glossaryDialog', {
            allowedContent: 'glossary[code]',
            requiredContent: 'glossary',
        } ) );

        editor.ui.addButton( 'Glossary', {
            label: 'Insert Glossary Entry',
            command: 'glossary',
            toolbar: 'insert'
        });

        if ( editor.contextMenu ) {
            editor.addMenuGroup( 'glossaryGroup' );
            editor.addMenuItem( 'glossaryItem', {
                label: 'Edit Glossary Entry',
                icon: this.path + 'icons/glossary.png',
                command: 'glossary',
                group: 'glossaryGroup'
            });

            editor.contextMenu.addListener( function( element ) {
                if ( element.getAscendant( 'glossary', true ) ) {
                    return { glossaryItem: CKEDITOR.TRISTATE_OFF };
                }
            });
        }

        CKEDITOR.dialog.add( 'glossaryDialog', this.path + 'dialogs/glossary.js' );
    }
});