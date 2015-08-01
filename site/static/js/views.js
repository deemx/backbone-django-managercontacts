/*
 * Global App View
 */
App.Views.App = Backbone.View.extend({
    initialize: function() {
        vent.on('contact:edit', this.editContact, this);
        
        var addContact = new App.Views.AddContact({ collection: App.contacts });
        var allContacts = new App.Views.Contacts(
            { collection: App.contacts }).render();
        $('#allContactsTable').append(allContacts.el);
    },

    editContact: function(contact) {
        var editContactView = new App.Views.EditContact(
            { model: contact });
        $('#contact-form-block').html( editContactView.el );
    }
});

/*
 * AddContact View
 */
App.Views.AddContact = Backbone.View.extend({
    initialize: function() {
        this.first_name = this.$('#first_name');
        this.last_name = this.$('#last_name');
        this.email_address = this.$('#email_address');
        this.description = this.$('#description');
    },
    
    el: '#contact-form',

    events: {
        'submit': 'addContact'
    },

    addContact: function(e) {
        e.preventDefault();

        var newContact = this.collection.create({
            first_name: this.first_name.val(),
            last_name: this.last_name.val(),
            email_address: this.email_address.val(),
            description: this.description.val()
        }, { wait: true });

        this.clearInps();
    },

    clearInps: function() {
        this.first_name.val('');
        this.last_name.val('');
        this.email_address.val('');
        this.description.val('');
    }
});

/*
 * Edit Contact View
 */

App.Views.EditContact = Backbone.View.extend({
    initialize: function() {
        this.render();

        this.form = this.$('#edit-contact-form');
        this.first_name = this.$('#edit_first_name');
        this.last_name = this.$('#edit_last_name');
        this.email_address = this.$('#edit_email_address');
        this.description = this.$('#edit_description');
        
    },

    events: {
        'submit #edit-contact-form': 'submit', 
        'click button.cancel': 'cancel'
    },

    cancel: function() {
        this.remove();
    },

    submit: function(e) {
        e.preventDefault();

        this.model.save({
            first_name: this.first_name.val(),
            last_name: this.last_name.val(),
            email_address: this.email_address.val(),
            description: this.description.val()
        });

        this.remove();
    },
    
    template: App.template('editContactTpl'),

    render: function() {
        var html = this.template( this.model.toJSON() );

        this.$el.html(html);
        return this;
    }
});

/*
 * All contacts view
 */

App.Views.Contacts = Backbone.View.extend({
    initialize: function() {
        this.collection.on('add', this.addOne, this);
    },

    tagName: 'tbody',

    render: function() {
        this.collection.each( this.addOne, this );

        return this;
    },

    addOne: function(contact) {
        var singleContact = new App.Views.Contact({ model: contact });
        this.$el.append( singleContact.render().el );
    }
});

/*
 * Single contact view
 */

App.Views.Contact = Backbone.View.extend({
    initialize: function() {
        this.model.on('destroy', this.unrender, this);
        this.model.on('change', this.render, this);
    },
    
    tagName: 'tr',

    events: {
        'click a.delete': 'removeContact',
        'click a.edit': 'editContact'
    },
    
    removeContact: function() {
        this.model.destroy();
    },

    unrender: function() {
        this.remove(); //this.$el.remove
    },

    editContact: function() {
        vent.trigger('contact:edit', this.model);       
    },
    
    template: App.template('contactTpl'),
    
    render: function() {
        this.$el.html( this.template( this.model.toJSON() ));
        return this;
    }
});
