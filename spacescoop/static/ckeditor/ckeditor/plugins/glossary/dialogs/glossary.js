function slugify(text)
{
    return text
        .toLowerCase()
        .replace(/ /g,'-')
        .replace(/[^\w-]+/g,'')
        ;
}


CKEDITOR.dialog.add( 'glossaryDialog', function( editor ) {
    return {
        title: 'Glossary entry',
        minWidth: 400,
        minHeight: 200,

        contents: [
            {
                id: 'tab-basic',
                label: 'Basic Settings',
                elements: [
                    {
                        type: 'text',
                        id: 'caption',
                        label: 'Text',
                        validate: CKEDITOR.dialog.validate.notEmpty( "Text field cannot be empty." ),

                        setup: function( text, slug ) {
                            this.setValue( text );
                        },

                        commit: function( element ) {
                            element.setText( this.getValue() );
                        }
                    },
                    {
                        type: 'text',
                        id: 'slug',
                        label: 'Slug',
                        requiredContent: 'glossary[slug]',
                        validate: CKEDITOR.dialog.validate.notEmpty( "Slug field cannot be empty." ),

                        setup: function( text, slug ) {
                            this.setValue( slug );
                        },

                        commit: function( element ) {
                            element.setAttribute( "slug", this.getValue() );
                        }
                    }
                ]
            }

        ],

        onShow: function() {
            var selection = editor.getSelection();
            var element = selection.getStartElement();

            if ( element )
                element = element.getAscendant( 'glossary', true );

            if ( !element || element.getName() != 'glossary' ) {
                element = editor.document.createElement( 'glossary' );
                this.insertMode = true;
            }
            else
                this.insertMode = false;

            this.element = element;

            if ( !this.insertMode ) {
                this.setupContent( this.element.getText(), this.element.getAttribute( "slug" ) );
            } else {
                this.setupContent( selection.getSelectedText(), slugify(selection.getSelectedText()) );
            }
        },

        onOk: function() {
            var dialog = this;
            var glossary = this.element;
            this.commitContent( glossary );

            if ( this.insertMode )
                editor.insertElement( glossary );
        }
    };
});